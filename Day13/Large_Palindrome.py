

debug = False
# to check palindrome
def isPalindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False
    
def solve(s):
    # logic to make combination of substring
    combinations = []
    for i in range(len(s)):
        # print(len(s))
        for j in range(i+1, len(s)+1):
                # print("adding elements between ", i, j, " are ", s[i:j])
                combinations.append(s[i:j])
    # for debugging purposes
    if debug == True:
        print("unique combinations of the string: ",combinations)

    # chech anf store plaindrome in that substrings 
    palindromes = []
    not_palindromes = []
    for i in combinations:
        if isPalindrome(i):
            palindromes.append(i)
        else:
            not_palindromes.append(i)
         
    if debug == True:
        print("Palindrome in the combinations: ",palindromes)
    
    return palindromes, not_palindromes

# solve("abba")

def main():
    # s = "asdfgfdsaqasdfgfdsaasdfgfdsaqasdfgfdsaasdfgfdsaqasdfgfdsaasdfgfdsaqasdfgfdsaasdfgfdsaqasdfgfdsaasdfg" # for 100 charecters
    # s = s+s+s+s+s # for 500 charecters
    # s = s+s # for 1000
    # s = s+s+s # for 3000
    s = "locnfkglorkkvxrnqbsqtipqonxtsnasonzvxbpiufdqmlglimklfzktgygdttnhcvpfdfbrpzlkvshwywshtdgmbqbkkxcvgumonmwtjkcalswqqhvyimhepyhhbtopsuqomfjrdyislifqgbndakaqbbwnkxnwpzeoohlxuhrtbfnqorfguvomeepxoffghmatidzfpfnwbfujdonliifcoktjpjxcjyiwchyicqibxdgkqtgqiwpdklhumzwljmgdmicmunnnpdbamofynykvytbytnuqhmfjaqtgngcwkuzyaumdgixjbcqvztzdjqmadthtdmvaqcagsyqggcfiifcoktjpjxcjyiwchyicqibxdgkqtgqiwpdklhumzwljmgdmicmunnnpdbamofynykqvsijsnfkpfyptlmqpoyjmeqvhcrvgmqmqopusqktdthpvztfzxrnqbsqtipqonxtsnasonzvxbpipyhhbtopsuqomfjrdyislifqgbndakaqbbwnkxnwpzeoohlxuhrtbfnqorfguvomeepxoffghmatidzfpfnwbfujdonlvyvwcwcchvsasdylbrrxfcztzqopdihybrhodjnmoqkijywkoncvrjozdpmnerphfmwevhwlezohyeehbrcewjxvceziftiqtntfsrptugtiznorvonzjfeacgamayapwlmbzitzszhzkosvnknberbltlkggdgpljfisyltmmfvhybljvkypcflsaqevcijcyrgmqirzniaxakholawoydvchveigttxwpukzjfhxbrtspfttotafsngqvoijxuvqbztvaalsehzxbshnrvbykjqlrzzfmlvyoshiktodnsjjpqplciklzqrxloqxrudygjtyzleizmeainxslwhhjwslqendjvxjyghrveuvphknqtsdtwxcktmwwwsdthzmlmbhjkmouhpbqurqfxgqlojmwsomowsjvpvhznbsilhhdkbdxqgrgedpzchrgefeukmcowoeznwhpiiduxdnnlbnmyjyssbsococdzcuunkrfduvouaghhcyvmlkzaajpfpyljtyjjpyntsefxiswjutenuycpbcnmhfuqmmidmvknyxmywegmtunodvuzygvguxtrdsdfzfssmeluodjgdgzfmrazvndtaurdkugsbdpawxitivdubbqeonycaegxfjkklrfkraoheucsvpiteqrswgkaaaohxxzhqjtkqaqhkwberbpmglbjipnujywogwczlkyrdejaqufowbigrsnjniegvdvotugocedktcbbufnxorixibbdfrzuqsyrfqghoyqevcuanuujszitaoaowsxyglafbwzddoznrvjqeyqignpitruijvyllsibobjltusrypanvybsfrxtlfmpdidtyozoolzslgdgowijatklvjzscizrkupmsoxftumyxifyunxucubvkfctkqlroqgzjvjwzizppvsomflvioemycnpkxgxsupmbntqrlwyampdgunxqdkhbwwefbvqsghhhutdgethcwupzrtsbhbjnbqwpccoaonxwvkhowbzhaoscgykzbiltlwqqatyeczzceuuwgvjxzonhkkfjcbwsezdmifdegsyjtswselknxweimxlnzohgtqthlftjblnphtdwwvsscbhjmruuqscwjpynxbkoomwdecqkrtbxgzgcxhppcjnqtcfqttkkolzcfikwblxkimijeglxsvcrkcqjjwcwuhvzydmegubqavlqffhrzzrhiwxrgftittdxcaybczncsyjlzlxyyklcppoxcgnexmaajzuhabdhaccuualacylsmtkewbprsmoncggqvrvsqqoffmwkplsgbrpurgioajuppvqluhbdetzdzwwzaelmopafumtqugecywglucmugwqiizveswrjevfzdnxlbkakrpzcejvxzeoybbtfdsvewjsivwswzjhudtpqsfclzcmukotirrxxtzksmxnjumofzhhowyftzfzbotrokaxaryxlkmueolqkrdxmzhoqnzvudeoigxldhlhqdyjcfhuqjfymrbafmyocttyjmnhlfnrtzddlazixtlxyvmvfbiguhsfuqoerhymsnoprkbdlchswocbbwwdvastaiamnepwkyaqmpliruphedkxjqzgpexlwulswtvotlgotlncpvnrrzerzdygeraoozbttnyyifkindeouuagqgztvqdolfrzrlzddjzcshvdgkhxkdxflwxmejkkszylbhoaacicwqiizickgcdxstpzkskjwdqegrearjrncmmkdelekbesuhquepjrnrzbllldgdmyrpglrhllwnqozywqlsccvsropvrnxtmkgiwfvqfkotpdznjinpobubzbvstkkvubuucilxyhjbcilfldibmyebrlcnvnuuqfvhwxoorbyyiigppuftqswpksfdxicemjbftgoabwrqdoudfbyjutkeqakoarruhwuznnlydivfelxvtggkkkjmxlwbkbklbwfsvrbadvraqovanlsmklnfjxxvzdjlpyurxpjcssebtpznwoytjefobdynaiukctgrzjxzirzosjuncvhfhcnhhrajahitnbkvwtifcoqepqyzwyazzkddxywvgqxofsyxngevsdbatvzmz"
    # s = "daataer"
    palindromes, not_palindromes = solve(s)
    # print("palindromes in the combinations are ",palindromes)
    print(f"number of strings characters: {len(s)} \nNumber of palindromes subtring: {len(palindromes)} \nNumber of non palindromes subtring: {len(not_palindromes)}")

if __name__ == "__main__":
     main()