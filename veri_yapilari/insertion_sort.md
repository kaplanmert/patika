# insertionsort
Insertion sort projesi



[22,27,16,2,18,6] -> Insertion Sort

Sırayla en küçük elemanı bulup onunla ilk elemanın yerini değiştirir
1-> [2,27,16,22,18,6]
daha sonrasında aynı adımları uygulayarak ikinci üçüncü dördüncü eleman şeklinde giderek, yerlerini değiştirerek sıralar.
2-> [2,6,16,22,18,27]
3->[2,6,16,22,18,27]
4->[2,6,16,18,22,27]
5->[2,6,16,18,22,27]
6->[2,6,16,18,22,27]
görüldüğü gibi listemiz sıralandı.

Big O gösterimi -> O(n^2)'dir.

Time Complexity: Average case: Aradığımız sayının ortada olması,Worst case: Aradığımız sayının sonda olması, Best case: Aradığımız sayının dizinin en başında olması.

Average Case : 16,18
Worst case : 27
Best case : 2

4. sorunun cevabı olarak ise, 18 sayısı görüldüğü average case kısmına girer.

[7,3,5,8,2,9,4,15,6]
1-> [2,3,5,8,7,9,4,15,6]
2-> [2,3,5,8,7,9,4,15,6]
3-> [2,3,4,8,7,9,5,15,6]
4-> [2,3,4,5,7,9,8,15,6]




