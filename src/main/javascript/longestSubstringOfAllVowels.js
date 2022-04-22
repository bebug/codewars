import assert from 'assert/strict';

var longestBeautifulSubstring = function(word) {
    let keyWords = "aeiou"
    let keyWordPos = 0
    let wordPos = 0
    let wordStart = -1
    let max = 0

    for (let i = 0; i < word.length; i++) {

        if (wordStart !== -1) {
            if (word.charAt(i) === keyWords.charAt(keyWordPos)) {
                wordPos = i + 1;
                if (keyWordPos + 1 === keyWords.length) {
                    let newMax = wordPos - wordStart
                    max = Math.max(max, wordPos - wordStart)
                }
            } else if (keyWords.length > keyWordPos && word.charAt(i) === keyWords.charAt(keyWordPos + 1)) {
                keyWordPos = keyWordPos + 1;
                wordPos = i + 1;
                if (keyWordPos + 1 === keyWords.length) {
                    let newMax = wordPos - wordStart
                    max = Math.max(max, wordPos - wordStart)
                }
            }
        }

        if (wordPos !== i + 1) {
            wordStart = -1;
        }
        if (wordStart === -1 && word.charAt(i) === keyWords.charAt(0)) {
            wordStart = i;
            keyWordPos = 0;
            wordPos = i + 1;
        }
    }

    return max;

};

assert.equal(2169, longestBeautifulSubstring("eieuuoeeueauueeoiiueaeuioeiiieioaouoeeoiiauiueiiuieueeeoaeaeoooiuauiaaueieoeeeeioauaouueiioeiaaaaooeaaaeoouoaoioauoaeuiioaiuuiaaaiieiuiuoiaeuuiooeiiuoaauoioeaeieaeeeiouieuaaaaaeoaeiaeeeaoaeooueieaaaeieooouueaueeiaiuoioiioieuoeeoeaaeeaauoaiaoaauaauioaueiaiooeoiiaiauaooiiauaiaoaoeaioeiaeeuueioauoueuaaiiouoeoeoiaeeooaauieoeaiueioiaieouiaeauaeiaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooouuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuiuaeouiioieouieeiuaeeuoiooioiiaoueioeuaeeoaauoaaeeaaoiuueoeaeoaaeueoueeiiiuiouieaiuoieeoooueiiiaeeuaaieeaaoiuuoeuoauouiieuaeeiueaeeeaaoieaeuiuoeuoaaiueieiouiiiaoueuuiuooeioaeooaeueouiaeuaaiueuoeeiouioiiueiueaaiuoaieuiaoeuoeaeaiuaaoeeuouiiioeeoueuuauoieiaoaeeaeioouoaiieueoauaoeeoeouaiaoaueioiuaooouiueuieuauieeoeaiouoaoeeeueuoeuieooaaaaaiuoououiuuueoioieueuueaueaeuaieueeaieioieuuuueoooueueoiaoiuuiooiauaaiiiiuoaaueeaiiaeaauaooooeaaeuiaaouooauaaaaiieiaeeeeeiauiiuaueieuieaoeeiauiuaueouaeoaaoiuaoiaiouaiaeoiaooieeioiieieioeeioeuioeiooouiiioaiaeeaaieouoaooaiaiueeuieoiuaeuieeiuaoaueiouoieauieiuoooieuiaooeaeaoiueaeeuieaioiuoaeieuaaeouuoiieioeoiaeuiiiuiuaaaoeaaaoiuauaiiuaaaaiieeueeoieuiueuaueiiaioaoaoueiieueoauuueeeeuuueoiuuaiaaeuauuiaeuuaeiaiiioiooeaeiaeoeaeouuaouueeiieaoaeoaueuaoouoioeiaiuiouaueuaiaoeouoeoooioiuioaeeoeaaoioeiioiuoaiiuioiiioeuiiaaaieaoaaeoaeieuiiiuieiieaaioaueoiiiuueeiouuueoiiaeuuaeaaiauaeeieoaioiiuueuaoieieiuiaioeaeuiiaioaieeeaoaieoooiuiaeuuuieeaeeeeuoeueioeiiaaieaiaiiieiouueaouoooueeoiauooeieeoeuoueioauieoeuooiiaiueeouiiuuiaiuuouoaaiuiiiouuuaiiiuiiuouiioaoauiaoeiioaooeuoaauaiiieiuueuueioeaioaaieuuoioeaeeeuauouuiaauuiauuuaiiiooaiaeaeeuioaueeaoiaioiieooueaieoeieoiaouuuuioaieauioeuoauauaaeaoueeiaaoooauoioueaieeaaiuuiieieaaaeoiueeoeoeoaaoioaueeoeoiooeiioiaoeieieaeiaaaoeeuoiueaueoeoaueeiioauuuoaiaeaooaiaaauuieaioeaaoeioouaiauiaaoieiiieeioeeuaiauuaeeooiuuuaeeieaeieoaaiioaoooeaaeaooouaaoeaoiiuaiauooaiuoeauoeiaeaaeueeiaiooaeaoioeuuauaioaiiioioeuuueiuaeoeaiiuaioiueooioeiueaaeueeiauoiaoeooiuaeuoaououiiiauuaaeeuaiuueaaoioueouaooaaiieeeiueieeouoieiuoueeueauauoueaooaoiuouuiauaeoiouaoeaauaaaoaaueoaeaoeuaiiiaueeiiaaoeuaouiaaiauoeeueueiaooeiooaeuooiieioaaeiueuieuoueiaeiiiaaueaaaoauiauaooaeoeouaaoeeoieuioeuooeaeeoioeeoouieiouuooeaioooouoaoeeouueioaeuoeoiioeouoeuiuuaaouaiuaioaiiuiiuuieaoiiieaaeeioeeiuuouioiuoaiuuuouoeauuoauoeiuuoiiuauoaeuieaiaaoaoiieoeeiaoaueuuoiaauioueeiueeaouioiiauoeuaooiueaaeuuiiiooioeiuioaeuuaouieeiuooaeeaeiiiaiieoaeeoaoioieiuiaeiaiiiouoeoeaeuiuaoeuiiouoaeioiouioiaouiaoooioooieiieaeeaiaaiuoaaaaeoauioiouaaaoeiiueaooeieieueaoiuiaiueaaauiuiuooeaaaaeoiooeueiaaueeaeaoouoioouoeouaoaooauieeuuoeooaauuoaueoaaauiiueoaauiiaaiaoaiuoeeooiiauaueeuoiuooaiueeeauaoeeaiieeoeaaaoueaeiouaouioauoouaeoiauaauouuuaoeuaaeueeeouoaouueaooiueeauuiiioeaeeieoaoeaooauaiiiueoaiauoueeiooueeiooiaouauiaoooioaaaaoeiaieoeaeaeeoaoaeeaeeuuuuioouaioeouuiuouuoeoaeeaaaeeaoooiaeieiuiuauouuieuiauooioiuoeeoieooeeouoiaaoueoaaiaiuauaauouiauiuoiioiiiauiuooiaooeeiuoeaoaeouuauueiueiuoioeiiaiioueeuiiiueoaieuueaoaiioeeuuauuuiuaueooeaaeeioieuieuuieaeoeoaaoeaoaoueiiaueuouiuuaauiiiuuoaaouaeioioooieoaioeouiiuoeaiaiiueoauaaiaeaaeouaeoiouieuaiaeuieuuioueiueueuaooiiouaioeuooeuaaoooieuauuaueiieoeiouaoaeuiaoaooeoeiaoieeaiiuaeaeauoaieeoeoeoauiauiaooouioaoiueuiueaueaaaoaouoeauueaieeuaiueiuauiueaoieoaioouiaaeuiiiueuaiuaiaeiaouooeioaoeaoiaieaeiuouaieeieoaiaaoioaeau"))
assert.equal(13, longestBeautifulSubstring("aeiaaioaaaaeiiiiouuuooaauuaeiu"))
assert.equal(0, longestBeautifulSubstring("a"))
assert.equal(5, longestBeautifulSubstring("aeeeiiiioooauuuaeiou"))
