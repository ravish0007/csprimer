
(def cache
  {0 {\0 0, \1 1, \2 2, \3 3, \4 4, \5 5, \6 6, \7 7, \8 8, \9 9}
   1 {\0 0, \1 2, \2 4, \3 6, \4 8, \5 1, \6 3, \7 5, \8 7, \9 9}})

(defn lookup [index-digit-vec]
  (let [index (first index-digit-vec)
        digit (last index-digit-vec)]
    (get (get cache (mod index 2)) digit)))

(defn verify [digits]
  (let [sum (reduce  + (doall (map lookup (map-indexed vector (reverse digits)))))]
    (= (mod sum 10) 0)))

(println (verify "17893729975"))
(println (verify "17893729974"))
