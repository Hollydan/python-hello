<?xml version='1.0' encoding='utf-8'?>

<bookstore>
    <book category='php'>
        <title>HTML</title>
        <author>html</author>
        <price>23</price>
    </book>
    <book category='python'>
        <title>HTML</title>
        <author>html</author>
        <price>23</price>
    </book>
    <book category='html'>
        <title>HTML</title>
        <author>html</author>
        <price>23</price>
    </book>
</bookstore>

'''
nodename
/   root node to find allnode
//  current node to find allnode
.   current node
..  parent node
@   select option

predicate

*
@*
node()

'''
'''
bookstore
/bookstore
/bookstore/book
//book
//@lang

/bookstore/book[1]
/bookstore/book[last()]
/bookstore/book[last()-1]
/bookstore/book[position()<3]
/bookstore/book[@lang]
/bookstore/book[@lang='cn-ZH']
/bookstore/book[@price < 100]
/bookstore/book[@price < 100]/title

//book/title | //book/author    select title and author
'''

