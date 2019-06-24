package accumulate

// Accumulate performs an operation on every item in a collection
func Accumulate(coll []string, op func(string)(string)) []string {
	newColl := []string{}
	for i := range(coll) {
		// newItem := op(coll[i])
		newColl = append(newColl, op(coll[i]))
	}
	return newColl
}