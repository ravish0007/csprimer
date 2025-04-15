fn verify_imperative(cc_string: &str) -> bool {
    let mut total = 0;

    for (i, c) in cc_string.chars().rev().enumerate() {
        let digit = c.to_digit(10).unwrap();
        if i % 2 == 1 {
            let mut digit_doubled = digit * 2;
            if digit_doubled > 9 {
                digit_doubled -= 9;
            }
            total += digit_doubled;
        } else {
            total += digit;
        }
    }

    return total % 10 == 0;
}

fn luhn_modulo_lookup(num: u32, multiplier: u32) -> u32 {
    let num = num * multiplier;
    if num > 9 {
        num - 9
    } else {
        num
    }
}

fn verify_functional(cc_string: &str) -> bool {
    let checksum = cc_string
        .chars()
        .map(|c| c.to_digit(10).unwrap())
        .rev()
        .enumerate()
        .fold(0, |acc, (i, val)| {
            let index = i as u32;
            acc + luhn_modulo_lookup(val, index % 2 + 1)
        });
    checksum % 10 == 0
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_invalid_credit_card_functional() {
        assert_eq!(verify_functional(&"17893729975"), false);
    }

    #[test]
    fn test_invalid_credit_card_imperative() {
        assert_eq!(verify_imperative(&"17893729975"), false);
    }

    #[test]
    fn test_valid_credit_card_functional() {
        assert_eq!(verify_functional(&"17893729974"), true);
    }

    #[test]
    fn test_valid_credit_card_imperative() {
        assert_eq!(verify_imperative(&"17893729974"), true);
    }
}

fn main() {
    println!("{}", "helloworld");
}
