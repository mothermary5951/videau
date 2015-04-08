for x in xrange(1, 6):
     if x == 5:    ## multiplies by 1 through 4; stops at 5
         break
     for y in xrange(1, 6): ## stopped  at 6
          if y == 6:     
              break
          else:
              print '%d * %d = %d' % (x, y, x * y)


##  output for above code:
# 1 * 1 = 1
# 1 * 2 = 2
# 1 * 3 = 3
# 1 * 4 = 4
# 1 * 5 = 5
# 2 * 1 = 2
# 2 * 2 = 4
# 2 * 3 = 6
# 2 * 4 = 8
# 2 * 5 = 10
# 3 * 1 = 3
# 3 * 2 = 6
# 3 * 3 = 9
# 3 * 4 = 12
# 3 * 5 = 15
# 4 * 1 = 4
# 4 * 2 = 8
# 4 * 3 = 12
# 4 * 4 = 16
# 4 * 5 = 20



## output with print '%d * %d = %d', (x, y, x * y)
##  %d * %d = %d (1, 5, 5)
##  %d * %d = %d (2, 5, 10)
##  %d * %d = %d (3, 5, 15)
##  %d * %d = %d (4, 5, 20)

## output with the formatter % - print '%d * %d = %d' % (x, y, x * y)
##  1 * 5 = 5
##  2 * 5 = 10
##  3 * 5 = 15
##  4 * 5 = 20

