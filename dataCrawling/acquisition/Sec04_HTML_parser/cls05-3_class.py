from bs4 import BeautifulSoup

text = '''
<!--
<style>
a.class1{
    font-size:30
}
</style>
-->
<a href=a.html class=class1>a</a>
<a href=b.html class="class1 class2">b</a>
<a href=c.html>c</a>
'''

soup = BeautifulSoup(text, 'html.parser')

for a in soup.select('a.class1'):
    print(a.text)