import math
import re

"""
    == Instructions ==
    Debug why the included test cases aren't succeeding and account for them in the code
    A description of the expected behaviour is given below
"""

def shortestDistance(document, word1, word2):

        
        
        """ Given two words returns the shortest distance between their two midpoints in number of characters.
            Words can appear multiple times in any order and should be case insensitive.
            E.g. for the document="This is a sample document we just made up"
            shortestDistance( document, "we", "just" ) == 4
            shortestDistance( document, "is", "a" ) == 2.5
            shortestDistance( document, "is", "not" ) == -1
        """
        # todo: determine why tests are failing
        words = re.split("[,. ]", document)
        index = 0
        shortest = len(document)
        word1Loc = 0
        word2Loc = 0
        
        for word in words:
#            lowered all words for the sake of comparison
            if word.lower().strip(",").strip(".") == word1.lower():
                word1Loc = index + (len(word)/2.0)
                
            elif word.lower().strip(",").strip(".") == word2.lower():
                word2Loc = index + (len(word)/2.0)

            if word1Loc > 0 and word2Loc > 0:
#               in case the order of the words are not in sequence. eg word2 appears before word1
                current = abs(word1Loc - word2Loc)
                if current < shortest:
                    shortest = current
            
#             Added plus one to account for spaces after each iteration
            index += len(word) + 1
            
        if word1Loc == 0 or word2Loc == 0:
            return -1

        return shortest;
def doTestsPass():
    """ Returns 1 if all tests pass. Otherwise returns 0. """
    # todo: implement more tests, please
    # feel free to make testing more elegant
    doPass = shortestDistance(document, "and", "graphic") == 6;
    
    doPass = doPass and shortestDistance(document, "transfer", "it") == 14;
    
    doPass = doPass and shortestDistance(document, "Design", "filler")== 25;
    
    doPass = doPass and shortestDistance(document, "It", "transfer") == 14;
    
    doPass = doPass and math.fabs(shortestDistance(document, "of", "lorem") - 4.5) < 0.000001;
    
    doPass = doPass and shortestDistance(document, "thiswordisnotthere", "lorem") == -1;
    # print doPass
   
    
    if doPass:
            print("All tests pass\n")
    else:
            print("There are test failures\n")

    return doPass

document =  "In publishing and graphic design, lorem ipsum is a filler text commonly used to demonstrate the graphic elements";
document += " of a document or visual presentation. Replacing meaningful content that could be distracting with placeholder text";
document += " may allow viewers to focus on graphic aspects such as font, typography, and page layout. It also reduces the need";
document += " for the designer to come up with meaningful text, as they can instead use hastily generated lorem ipsum text. The";
document += " lorem ipsum text is typically a scrambled section of De finibus bonorum et malorum, a 1st-century BC Latin text by";
document += " Cicero, with words altered, added, and removed to make it nonsensical, improper Latin. A variation of the ordinary";
document += " lorem ipsum text has been used in typesetting since the 1960s or earlier, when it was popularized by advertisements";
document += " for Letraset transfer sheets. It was introduced to the Information Age in the mid-1980s by Aldus Corporation, which";
document += " employed it in graphics and word processing templates for its desktop publishing program, PageMaker, for the Apple";
document += " Macintosh. A common form of lorem ipsum reads: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do";
document += " eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation";
document += " ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit";
document += " esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui";
document += " officia deserunt mollit anim id est laborum.";

if __name__ == "__main__":
        doTestsPass()