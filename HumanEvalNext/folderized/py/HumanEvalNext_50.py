def decode_shift(s: str) -> str:
    """
    Takes as input a lowercase string encoded as follows:
        - Shift every letter by 5 in the alphabet.
    
    This function should return the decoded string.

    Examples:
        >>> decode_shift("cryim")
        "xmtdh"
        >>> decode_shift("zlsebmzxbqrvxkrwlqvrvgpmbrgerh")
        "ugnzwhuswlmqsfmrglqmqbkhwmbzmc"
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])


def check(candidate):
    assert candidate("cryim") == "xmtdh"
    assert candidate("zlsebmzxbqrvxkrwlqvrvgpmbrgerh") == "ugnzwhuswlmqsfmrglqmqbkhwmbzmc"
    assert candidate("cfxchfesawcaybmbq") == "xasxcaznvrxvtwhwl"
    assert candidate("qenusc") == "lzipnx"
    assert candidate("awxsembugkohodgmfgukoe") == "vrsnzhwpbfjcjybhabpfjz"
    assert candidate("jqpwtvyugwxdufxufmfomuvdhr") == "elkroqtpbrsypaspahajhpqycm"
    assert candidate("xcbsxxv") == "sxwnssq"
    assert candidate("vsqqqtyijuqrpwhwujfjwwroyki") == "qnlllotdeplmkrcrpeaerrmjtfd"
    assert candidate("zvegyx") == "uqzbts"
    assert candidate("cy") == "xt"
    assert candidate("wprutqdnzgsszkdrfxr") == "rkmpolyiubnnufymasm"
    assert candidate("ncnysltpwero") == "ixitngokrzmj"
    assert candidate("rz") == "mu"
    assert candidate("d") == "y"
    assert candidate("nfmtxc") == "iahosx"
    assert candidate("ajzljqbqmjcoaonfhwoqaegzcdtys") == "veugelwlhexjvjiacrjlvzbuxyotn"
    assert candidate("wrxewhq") == "rmszrcl"
    assert candidate("qhreoflzkcavertgwjjkqpelf") == "lcmzjagufxvqzmobreeflkzga"
    assert candidate("efgcpgvastfvfbeqim") == "zabxkbqvnoaqawzldh"
    assert candidate("ciesqujkrpqaicsalggqqglbgefda") == "xdznlpefmklvdxnvgbbllbgwbzayv"
    assert candidate("lvwdatspdknfophedb") == "gqryvonkyfiajkczyw"
    assert candidate("bvslymhi") == "wqngthcd"
    assert candidate("r") == "m"
    assert candidate("csyaezdhltsjqf") == "xntvzuycgonela"
    assert candidate("wmfhficemirrar") == "rhacadxzhdmmvm"
    assert candidate("qnxqfesaqqylwgagkoedpyzlu") == "lislaznvlltgrbvbfjzyktugp"
    assert candidate("zcnadqxvcdcpcktvoupjoprphy") == "uxivylsqxyxkxfoqjpkejkmkct"
    assert candidate("") == ""
    assert candidate("cpgrgqcouxqjhmhmeb") == "xkbmblxjpslechchzw"
    assert candidate("lscnjxwtjo") == "gnxiesroej"
    assert candidate("ovrccha") == "jqmxxcv"
    assert candidate("vqpndvzdr") == "qlkiyquym"
    assert candidate("vdlv") == "qygq"
    assert candidate("hllmxekoolweyfylutlidd") == "cgghszfjjgrztatgpogdyy"
    assert candidate("nnrmr") == "iimhm"
    assert candidate("f") == "a"
    assert candidate("tjjedyqwarzojllekcylkdtfrben") == "oeezytlrvmujeggzfxtgfyoamwzi"
    assert candidate("yoftxdujbzlypbzvsrbxgxjgivufjl") == "tjaosypewugtkwuqnmwsbsebdqpaeg"
    assert candidate("biv") == "wdq"
    assert candidate("b") == "w"
    assert candidate("zxywijupundpzgdamccgad") == "ustrdepkpiykubyvhxxbvy"
    assert candidate("ebqofwhlhsrqfcdhzzn") == "zwljarcgcnmlaxycuui"
    assert candidate("nkqxezekxywvxbfxzrc") == "iflszuzfstrqswasumx"
    assert candidate("dmhbyemucgzyzsrdfwrvcdqlgnmnx") == "yhcwtzhpxbutunmyarmqxylgbihis"
    assert candidate("rnvs") == "miqn"
    assert candidate("c") == "x"
    assert candidate("i") == "d"
    assert candidate("btwdciurccoracrovdzlxeowoz") == "woryxdpmxxjmvxmjqyugszjrju"
    assert candidate("bfqfozpjznetrumo") == "walajukeuizomphj"
    assert candidate("egkfxtcnu") == "zbfasoxip"
    assert candidate("") == ""


def test_check():
    check(decode_shift)