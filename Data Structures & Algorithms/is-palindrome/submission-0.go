func isPalindrome(s string) bool {
    t:=strings.ToLower(strings.TrimSpace(s))
    var r []rune

    for _,char := range t{
        if unicode.IsLetter(char) || unicode.IsDigit(char){
                r = append(r,char)
        }
    }
    left, right := 0, len(r)-1
    for left <=right {
        if r[left] != r[right]{
            return false
        }
        left ++
        right --
   }
   return true
}