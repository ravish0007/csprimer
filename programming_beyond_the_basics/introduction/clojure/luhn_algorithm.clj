(def mod-9s {0 0, 1 1, 2 2, 3 3, 4 4, 5 5, 6 6, 7 7, 8 8, 9 9, 10 1, 12 3, 14 5, 16 7, 18 9 })

(defn lookup-luhn-mod [multiplier digit]
  (mod-9s (* multiplier digit)))


;; type hinting makes much faster
(defn parse-cc [^String cc-string]
  (map #(Character/digit ^Character % 10) cc-string))

(defn debug [x]
  (println x) 
  x
  )

(defn verify-cc? [digits]
  (->>  digits
        (reverse)
        (map lookup-luhn-mod (cycle [1 2])) 
        (reduce +)
        ( #(mod % 10 ))
        (zero?)
    ))
(defn parse-n-verify-cc? [cc-string]
  (-> cc-string
      parse-cc
      verify-cc?))

(println (parse-n-verify-cc? "17893729975"))
(println (parse-n-verify-cc? "17893729974"))



