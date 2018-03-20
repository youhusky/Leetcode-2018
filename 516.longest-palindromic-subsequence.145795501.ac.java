/*
 * [516] Longest Palindromic Subsequence
 *
 * https://leetcode.com/problems/longest-palindromic-subsequence/description/
 *
 * algorithms
 * Medium (42.78%)
 * Total Accepted:    28.3K
 * Total Submissions: 66.1K
 * Testcase Example:  '"bbbab"'
 *
 * 
 * Given a string s, find the longest palindromic subsequence's length in s.
 * You may assume that the maximum length of s is 1000.
 * 
 * 
 * Example 1:
 * Input: 
 * 
 * "bbbab"
 * 
 * Output: 
 * 
 * 4
 * 
 * One possible longest palindromic subsequence is "bbbb".
 * 
 * 
 * Example 2:
 * Input:
 * 
 * "cbbd"
 * 
 * Output:
 * 
 * 2
 * 
 * One possible longest palindromic subsequence is "bb".
 * 
 */
public class Solution {
    public int longestPalindromeSubseq(String s) {
        int len=s.length();
        int[][] dp=new int[len][len];
        for (int i=0;i<len;i++)
            dp[i][i]=1;
        for (int d=1;d<len;d++) {
            for (int i=0;i<len-d;i++) {
                int j=i+d;
                if (s.charAt(i)==s.charAt(j)) dp[i][j]=2+dp[i+1][j-1];
                else dp[i][j]=Math.max(dp[i][j-1], dp[i+1][j]);
            }
        }
        return dp[0][len-1];
    }
}
