;; author jaihindhreddy

(ns scratch
  (:require [criterium.core :as crit]
   [clojure.pprint :as pp]))

; arguably reads the easiest of these.
(defn valid-luhn-0? [^String s]
  (->
    (->> (reverse s)
      (map #(Character/digit % 10))
      (map * (cycle [1 2]))
      (map #(if (> % 9) (- % 9) %))
      (reduce + 0))
    (mod 10)
    zero?))

; same as prev, but with the type-hint eliminating reflection in Character/digit call.
(defn valid-luhn-0b? [^String s]
  (->
    (->> (reverse s)
      (map #(Character/digit ^Character % 10))
      (map * (cycle [1 2]))
      (map #(if (> % 9) (- % 9) %))
      (reduce + 0))
    (mod 10)
    zero?))

; util for the following impls
(defn- luhn-shift [^long d]
  (let [d (* d 2)]
    (if (> d 9) (- d 9) d)))

; largely the same, but avoids intermediate-seqs, using transducers.
(defn valid-luhn-1? [^String s]
  (-> (transduce
        (map-indexed #(let [d (Character/digit ^Character %2 10)]
                        (if (even? %) d (luhn-shift d))))
        + 0 (reverse s))
    (mod 10)
    zero?))

; manually looping over the string, avoiding the sequence allocation in `(reverse s)`.
(defn valid-luhn-2? [^String s]
  (let [n (.length s)]
    (loop [i 0, sum 0]
      (if (= i n)
        (zero? (mod sum 10))
        (let [d (Character/digit (.charAt s (- n i 1)) 10)]
          (recur (inc i)
            (+ sum
              (if (even? i) d (luhn-shift d)))))))))

; same as prev but we're jumping two chars at a time, reducing conditionals inside the loop.
(defn valid-luhn-3? [^String s]
  (let [n (.length s)]
    (loop [i (dec n), sum 0]
      (cond (= i -1) (zero? (mod sum 10))
        (= i 0) (zero? (mod (+ sum (Character/digit (.charAt s 0) 10)) 10))
        :else
        (let [d1 (Character/digit (.charAt s i) 10)
              d2 (Character/digit (.charAt s (dec i)) 10)]
          (recur (- i 2)
            (+ sum d1 (luhn-shift d2))))))))

; loop from start to end as opposed to reverse, which may be beneficial for long strings.
(defn valid-luhn-4? [^String s]
  (let [n (.length s)]
    (loop [i (if (even? n) 0 1)
           sum (if (even? n) 0 (Character/digit (.charAt s 0) 10))]
      (if (= i n)
        (zero? (mod sum 10))
        (let [d1 (Character/digit (.charAt s i) 10)
              d2 (Character/digit (.charAt s (inc i)) 10)]
          (recur (+ i 2)
            (+ sum d2 (luhn-shift d1))))))))

; returns failing test-cases
(defn t [f]
  (->> [["17893729975" false]
        ["17893729974" true]
        ["178937299742" false
         "178937299745" true]]
    (filterv (fn [[i o]]
               (not= o (f i))))))

;; The other impls pass these cases too.
(t valid-luhn-0?) ; []

; util to measure one call.
(defn bench [f-sym input-str]
  (let [fmt #(let [[factor unit] (crit/scale-time %)]
               (crit/format-value % factor unit))
        f (resolve f-sym)
        {[mean] :mean, [variance] :variance}
        (crit/quick-benchmark (f input-str) {})]
    {:name f-sym
     :mean (fmt mean)
     :std-dev (fmt (Math/sqrt variance))}))

; measure all impls on this string.
(def res1
  (mapv #(bench % "178937299745")
    '[valid-luhn-0?
      valid-luhn-0b?
      valid-luhn-1?
      valid-luhn-2?
      valid-luhn-3?
      valid-luhn-4?]))
(pp/print-table res1)
;|          :name |         :mean |      :std-dev |
;|----------------+---------------+---------------|
;|  valid-luhn-0? |  27.123235 µs | 631.309552 ns |
;| valid-luhn-0b? |   2.486823 µs |  16.928762 ns |
;|  valid-luhn-1? | 750.081918 ns |  30.947325 ns |
;|  valid-luhn-2? | 113.483315 ns |   0.846319 ns |
;|  valid-luhn-3? |  48.647473 ns |   0.456904 ns |
;|  valid-luhn-4? |  50.588961 ns |   0.258768 ns |


; check whether looping forwards is better for long strings.
; result: doesn't seem to be.
(def res2
  (mapv #(bench % (apply str (take 30000 (cycle "178937299745"))))
    '[valid-luhn-3?
      valid-luhn-4?]))
(pp/print-table res2)
;|         :name |        :mean |    :std-dev |
;|---------------+--------------+-------------|
;| valid-luhn-3? | 89.405521 µs | 3.602098 µs |
;| valid-luhn-4? | 88.721100 µs | 2.968964 µs |
