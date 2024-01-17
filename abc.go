package main

import (
	"encoding/json"
	"fmt"
)

type Score struct {
	Korean  uint `json:"korean,omitempty"`
	Math    uint `json:"math,omitempty"`
	English uint `json:"english,omitempty"`
}

type KScore struct {
	Korean  uint `json:"korean,omitempty"`
	Math    uint `json:"math"`
	English uint `json:"english,omitempty"`
}

var s = &Score{
	Korean:  1,
	English: 4,
}

var k = &KScore{
	Korean:  123,
	English: 123,
}

func main() {
	var ss KScore
	// var ks KScore
	js, _ := json.Marshal(k)

	string_js := string(js)
	fmt.Printf("JSON String: %s\n", string_js)
	json.Unmarshal([]byte(string_js), &ss)

	fmt.Printf("Score: %+v", ss)

	// jk, _ := json.Marshal(k)
	// json.Unmarshal(jk, &ks)

	// fmt.Printf("KScore: %+v", ks)
}
