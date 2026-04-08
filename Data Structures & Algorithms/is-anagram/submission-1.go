func isAnagram(s string, t string) bool {
    if len(s)!=len(t){
        return false
    }

    c1 := []byte(s)
    c2 := []byte(t)

    sort.Slice(c1,func(i,j int)bool{
        return c1[i]<c1[j]
    })

    sort.Slice(c2,func(i,j int) bool{
        return c2[i]<c2[j]
    })

    if string(c1) == string(c2){
        return true
    }else {
        return false
    }
}
