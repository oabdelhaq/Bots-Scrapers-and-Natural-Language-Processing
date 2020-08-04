Facebook Data Read Me

There are three json files, one for each Facebook page: IRS, Florida Department of Economic Oportunity, and USPS.

IRS: Includes 80 most recent posts, post content, author, timestamp, comments, usernames, likes per comment, and replies to that comment.

FLDEO: Includes 50 most recent posts, post content, author, timestamp, comments, usernames, likes per comment, and replies to that comment.

USPS: Includes 80 most recent posts, post content, author, timestamp, comments, usernames, likes per comment, and replies to that comment.

Important to note:

The files are dirty with unicode. Each new post is marked with ie. 'IRS\n'.

When a comment with more than one reply is scraped, the original comment is duplicated then followed by replies.

The number of likes on a comment/reply is separated by unicode. So the number is shown, followed by a unicode string, followed by the word 'Likes'.
