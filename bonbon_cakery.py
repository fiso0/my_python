import itertools
import logging

logging.basicConfig(level=logging.DEBUG)

CAKE_NUM = 27 # 5
SHELF_NUM = 4
TOTAL_MONTH = 12

# cake_points = {\
# 'Jan':2,\
# 'Feb':1,\
# 'Mar':2,\
# 'Apr':2,\
# 'May':4,\
# 'Jun':4,\
# 'Jul':4,\
# 'Aug':2,\
# 'Sep':3,\
# 'Oct':1,\
# 'Nov':3,\
# 'Dec':3\
# }

'''
	Honey Choco Jiggle
	Choco Stick Torte
	Choco Cream Baum
	Whipped Cream Cream Cotta
	Whipped Cream Almond Ring
	Gentle Silver Cake
	Rich Fresh Feuille
	Vanilla Soy Flour Bavarian
	Velvety Roll Gelato
	Velvety Japanese Chocolate
	Choco Deluxe Chocolate
	Choco Sprinkle Waffle
	Rich Amande Creamy
	Roll Silver Waffle
	Sun Deluxe Feuille
	Velvety Deluxe Cotta
	Sun Silver Pudding
	Choco Big Gelato
	Whipped Cream Deluxe Vanilla Current Trend
	Velvety Chocolate
	Wipped Cream Decor Noel
	Chocho Choco Roll
	Whipped Cream Soy Flour Feuille Current Trend
	Whipped Cream Roll
	Star Japanese Puff
	Choco Japanese Waffle
	Choco Velvety Donut
	Sakura Cream Bavarian
'''
cake_lists_origin = [\
[4,1,5,4,2,1,4,2,3,1,5,1],\
[2,4,2,1,1,2,2,1,1,5,5,5],\
[2,3,2,2,1,1,4,2,5,5,3,3],\
[3,3,5,4,1,1,3,2,2,2,4,1],\
[4,2,1,3,1,2,1,3,4,5,4,4],\
[5,2,2,2,5,5,2,2,2,2,5,3],\
[2,1,2,2,4,4,4,2,3,1,3,3],\
[4,1,5,5,1,1,2,2,1,1,5,3],\
[4,1,3,1,2,1,5,5,3,1,5,1],\
[2,4,1,3,1,2,1,3,1,4,5,5],\
[2,3,2,2,1,1,2,2,1,3,5,5],\
[5,5,2,1,1,1,2,1,1,1,5,2],\
[5,5,1,3,1,2,3,3,3,2,2,4],\
[5,5,1,2,1,3,3,2,3,3,2,3],\
[2,1,2,2,4,4,4,2,3,1,3,3],\
[3,1,5,4,1,1,3,2,2,1,4,1],\
[3,1,5,4,1,1,3,2,2,1,4,1],\
[1,3,4,3,1,1,5,5,2,1,2,3],\
[3,2,1,2,1,2,5,5,2,2,3,2],\
[1,3,2,1,1,1,3,2,2,3,5,4],\
[1,3,2,2,1,1,3,3,5,5,2,2],\
[2,3,2,1,1,1,2,1,4,5,3,2],\
[2,1,2,2,4,4,4,2,3,1,3,3],\
[2,3,2,1,1,1,4,1,5,4,3,2],\
[5,4,3,1,2,1,5,1,4,1,4,2],\
[5,5,2,2,1,1,4,2,3,1,3,3],\
[4,3,2,1,1,1,2,1,4,4,5,2],\
[4,1,4,4,2,1,2,2,3,1,3,1]
]

cake_lists_good = [\
[4,0,5,4,0,0,4,0,0,0,5,0],\
[0,4,0,0,0,0,0,0,0,5,5,5],\
[0,0,0,0,0,0,4,0,5,5,0,0],\
[0,0,5,4,0,0,0,0,0,0,4,0],\
[4,0,0,0,0,0,0,0,4,5,4,4],\
[5,0,0,0,5,5,0,0,0,0,5,0],\
[0,0,0,0,4,4,4,0,0,0,0,0],\
[4,0,5,5,0,0,0,0,0,0,5,0],\
[4,0,0,0,0,0,5,5,0,0,5,0],\
[0,4,0,0,0,0,0,0,0,4,5,5],\
[0,0,0,0,0,0,0,0,0,0,5,5],\
[5,5,0,0,0,0,0,0,0,0,5,0],\
[5,5,0,0,0,0,0,0,0,0,0,4],\
[5,5,0,0,0,0,0,0,0,0,0,0],\
[0,0,0,0,4,4,4,0,0,0,0,0],\
[0,0,5,4,0,0,0,0,0,0,4,0],\
[0,0,5,4,0,0,0,0,0,0,4,0],\
[0,0,4,0,0,0,5,5,0,0,0,0],\
[0,0,0,0,0,0,5,5,0,0,0,0],\
[0,0,0,0,0,0,0,0,0,0,5,4],\
[0,0,0,0,0,0,0,0,5,5,0,0],\
[0,0,0,0,0,0,0,0,4,5,0,0],\
[0,0,0,0,4,4,4,0,0,0,0,0],\
[0,0,0,0,0,0,4,0,5,4,0,0],\
[5,4,0,0,0,0,5,0,4,0,4,0],\
[5,5,0,0,0,0,4,0,0,0,0,0],\
[4,0,0,0,0,0,0,0,4,4,5,0],\
[4,0,4,4,0,0,0,0,0,0,0,0]
]

cake_lists = cake_lists_good
best_min_pt = 0
best_min_pt_num = 0
best_pt_sum = 0

recipe_combs = list(itertools.combinations(range(CAKE_NUM),SHELF_NUM))
# [(0, 1, 2, 3), (0, 1, 2, 4), (0, 1, 3, 4), (0, 2, 3, 4), (1, 2, 3, 4)]

for each_comb in range(len(recipe_combs)): # 1~5
	logging.debug('combination '+str(each_comb))

	cakes_no = recipe_combs[each_comb] # 1*4 cakes number on shelves
	logging.debug('cakes numbers: '+str(cakes_no))

	total_pt = [0]*12 # 1*12 total points of cakes on shelves
	cakes_pt = [] # 4*12 points of cakes on shelves

	for each_shelf in range(SHELF_NUM): # 1~4
		current_pt_list = cake_lists[cakes_no[each_shelf]]
		logging.debug('points of cake on shelf '+str(each_shelf)+': '+str(current_pt_list))

		cakes_pt.append(current_pt_list)
		for month in range(TOTAL_MONTH): # 1~12
			total_pt[month] += current_pt_list[month]

	logging.debug('total points: '+str(total_pt)) # [12, 7, 11, 11, 8, 8, 12, 12, 8, 7, 18, 12]

	current_min_pt = min(total_pt)
	current_min_pt_bum = total_pt.count(current_min_pt)
	current_pt_sum = sum(total_pt)
	logging.debug('minimum point of this combination: '+str(current_min_pt))
	logging.debug('count of minimum point of this combination: '+str(current_min_pt_bum))
	logging.debug('sum points of this combination: '+str(current_pt_sum))

	if (current_min_pt > best_min_pt) or (current_min_pt == best_min_pt and current_min_pt_bum < best_min_pt_num)\
			or (current_min_pt == best_min_pt and current_min_pt_bum == best_min_pt_num and current_pt_sum > best_pt_sum):
		best_min_pt = current_min_pt
		best_min_pt_num = current_min_pt_bum
		best_pt_sum = current_pt_sum
		best_cake_comb = cakes_no
		best_total_pt = total_pt

print('best combination: '+str([no+1 for no in best_cake_comb]))
print('best total points: '+str(best_total_pt))
print('minimum point of this combination: ' + str(best_min_pt))
input('end')
