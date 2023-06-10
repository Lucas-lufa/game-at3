
class User_Interface:
    """ To display the text on the screen """

    scene = "enter a tile it will describe what is there. The environment, type of tile(bush, forest, beach) then the items(shrubs, trees, rocks) and items that can be picked up(backpack, sticks, small rocks, letters), navigation options describe the next tiles can move and is dangerous? ( the environment and not moveable items,). The description of scene and navigation options will stay up until move to the next tile. "

    w = "W print( item_describe_one , item_describe_two ) the play area will be ringed by dangerous tiles. total grid five by five but playable would be four by four."

    a = "A if go out of bounds the player dies. If player move will do this give a warning and a chance to back out. To move, up minus four, right plus one, down plus four, left minus one to your index."

    s = "S print( item_describe_one , item_describe_two ) the play area will be ringed by dangerous tiles. total grid five by five but playable would be four by four."

    d = "D if go out of bounds the player dies. If player move will do this give a warning and a chance to back out. To move, up minus four, right plus one, down plus four, left minus one to your index."

    examine = ""

    #print ("*"* 120)

    # if w scene and d return all blank spaces print d
    
    def cutup_strings(self, block, string_to_cut, padding, beginning_index=0):
        """ Cuts up strings into chunks:
            need the length to chunk
            need the delimiter """
        
        index_cut = beginning_index + block
        if string_to_cut[-1] != " ":
            string_to_cut = string_to_cut + " "
        if index_cut > len(string_to_cut):
            index_cut = len(string_to_cut) -1
        if string_to_cut[index_cut] != " ":
            index_cut += 2
        while string_to_cut[index_cut] != " ":
            index_cut -= 1

        if string_to_cut[index_cut] == " ":
            cut_string = string_to_cut[beginning_index:index_cut].strip()

            padding = padding - len(cut_string)
            left_padding = padding /2
            right_padding = padding - int(left_padding)
            cut_string = int(left_padding) * " " + cut_string + right_padding * " "
            return cut_string ,index_cut

    def user_interface_test(self):
        #self = User_Interface()
        #print(e.cutup_strings(15, e.a, 20)+"|"+e.cutup_strings(55, e.scene, 60)+"|"+e.cutup_strings(15, e.scene, 20))
        print()
        p1, i1 = self.cutup_strings(15, self.a, 20)
        p2, i2 = self.cutup_strings(55, self.scene, 60)
        p3, i3 = self.cutup_strings(15, self.d, 20)
        all_parts_print = p1+p2+p3
        print(all_parts_print)
        while not all_parts_print.isspace():
            p1, i1 = self.cutup_strings(15, self.a, 20, i1)
            p2, i2 = self.cutup_strings(55, self.scene, 60, i2)
            p3, i3 = self.cutup_strings(15, self.d, 20, i3)
            all_parts_print = p1+p2+p3
            print(all_parts_print)
        print()

if __name__ == "__main__":
    e = User_Interface()
    e.user_interface_test()