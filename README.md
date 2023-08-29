# Perfect_Matchups

Using counting and radix sort to find the best composition between each team

## Input

The matches's data is presented as a list of lists.The inner list can be
described as [t1, t2, score] where:
<p>The first match of result in the example is ['EAE', 'BCA', 85], which means that: <br>
- A team of 1 A character and 2 E characters (AEE)
has a score of 85 against
a team of 1 A character, 1 B character and 1 C character (ABC). <br>
- A team of 1 A character, 1 B character and 1 C character (ABC)
has a score of 15 against
a team of 1 A character and 2 E characters (AEE). </p>

## Output
1. top10matches is a list of 10 matches with the highest score.
2. searchedmatches is a list of matches with the same score as score.
<blockquote>
   a. The returned matches are sorted rstly in ascending lexicographical order for team1, and secondly in ascending lexicographical order for team2 (where team1 is the same). <br>
  b. If there are matches between the same teams, only one of the matches would be
included.  <br>
  c . If the score is not found, then return the matches with the closest score which is
higher. If there are no matches with a higher score, then return an empty list.
</blockquote>
