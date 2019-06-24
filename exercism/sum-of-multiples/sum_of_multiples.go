package summultiples

//SumMultiples gets the sum of the multiples of divisors up to
func SumMultiples(n int, multiples []int) int {

	var sum int
	
	var multi = []int{}

	for i := 0; i < n; i++ {
		for _, v := range multiples {

			if v == 0 {
				break
			}

			if i >= v && i%v == 0 {
				if len(multi) > 0 {
					for _, j := range multi {
						if i == j {
							sum = sum - i
							break
						}
					}
				}
				sum += i
				multi = append(multi, i)
			}
		}
	}
	return sum
}
