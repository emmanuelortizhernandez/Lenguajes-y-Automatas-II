<<<<<<< HEAD
=======
//comentario infiltrado
//otro comentario infiltrado
>>>>>>> 7322edf98a43542b8c33c3bdcb8f07d1169c8ab2
package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func main() {
	path := "archivo.js"

	buf, err := os.Open(path)
	if err != nil {
		log.Fatal(err)
	}

	defer func() {
		if err = buf.Close(); err != nil {
			log.Fatal(err)
		}
	}()

	r := bufio.NewReader(buf)
	b := make([]byte, 1)
	for {
		n, err := r.Read(b)
		if err != nil {
			fmt.Println("Error reading file:", err)
			break
		}
        c := string(b[0:n]) 
        if c != " "{
            fmt.Println(c)
        }
	}
}
