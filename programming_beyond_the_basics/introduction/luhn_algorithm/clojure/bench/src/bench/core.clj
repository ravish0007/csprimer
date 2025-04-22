(ns bench.core
  (:require [criterium.core :as crit]
   [clojure.pprint :as pp]))

(def mod-9s {0 0, 1 1, 2 2, 3 3, 4 4, 5 5, 6 6, 7 7, 8 8, 9 9, 10 1, 12 3, 14 5, 16 7, 18 9 })

(defn lookup-luhn-mod [multiplier digit]
  (mod-9s (* multiplier digit)))


(defn parse-cc-type-hinted? [^String cc-string]
  (map #(Character/digit ^Character % 10) cc-string))

(defn parse-cc [cc-string]
  (map #(Character/digit  % 10) cc-string))

(defn parse-cc-with-int [cc-string]
  (mapv #(- (int %) 48) cc-string))

(defn verify-cc? [digits]
  (->>  digits
        (reverse)
        (map lookup-luhn-mod (cycle [1 2])) 
        (reduce +)
        ( #(mod % 10 ))
        (zero?)))

(defn parse-n-verify-cc? [cc-string]
  (-> cc-string
      parse-cc
      verify-cc?))

(defn parse-n-verify-cc-hinted? [cc-string]
  (-> cc-string
      parse-cc-type-hinted?
      verify-cc?))

(defn parse-n-verify-cc-int-method? [cc-string]
  (-> cc-string
      parse-cc-with-int
      verify-cc?))

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

(defn control [sum]
  (mod (- 10 (mod sum 10)) 10))

(defn digit-value-2 [i d]
  (cond
    (odd? i) d
    (> d 4) (- (* 2 d) 9)
    :else (* 2 d)))

(defn checksum-2 [digits]
  (transduce (map-indexed digit-value-2) + digits))

(defn verify-2 [digits]
  (let [[hd & tl] (mapv #(- (int %) 48) (reverse digits))]
    (= hd (control (checksum-2 tl)))))


; measure all impls on this string.
(def res
  (mapv #(bench % "178937299745")
    '[parse-n-verify-cc?
      verify-2
      parse-n-verify-cc-hinted?]))
(pp/print-table res)

(defn -main []
  (println (parse-n-verify-cc-int-method? "178937299745")))
  ;; (res ))
