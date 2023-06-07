package main
 
import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
	"strings"
<<<<<<< HEAD
=======
	"hola que hace"
>>>>>>> 7322edf98a43542b8c33c3bdcb8f07d1169c8ab2
)
 
func main() {
	filename := "archivo.js"
 
	filebuffer, err := ioutil.ReadFile(filename)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	inputdata := string(filebuffer)
	data := bufio.NewScanner(strings.NewReader(inputdata))
	data.Split(bufio.ScanRunes)
 
	for data.Scan() {
        char := data.Text()
		fmt.Print(char)
        if char == ";" {
            fmt.Print("<<<<<<----------------- encontre un punto y coma")
        }
	}
}
