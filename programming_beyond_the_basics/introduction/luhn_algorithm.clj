(defn lookup [digit]
  (if (> digit  9) (- digit 9) digit))

(defn map-digit [index-digit-vec]
  (let [index (nth index-digit-vec  0)
        digit (Character/digit (nth index-digit-vec 1) 10)]
    (if (odd? index) (lookup (* digit 2)) digit)))

(defn verify [digits]
  (let [sum (reduce  + (doall (map map-digit (map-indexed vector (reverse digits)))))]
    (if (= (mod sum 10) 0) true false)))

(println (verify "17893729975"))
(println (verify "17893729974"))
