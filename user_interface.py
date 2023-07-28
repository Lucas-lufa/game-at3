
class UserInterface:
    """ To display the text on the screen """

    scene = "enter a tile it will describe what is there. The environment, type of tile(bush, forest, beach) then the items(shrubs, trees, rocks) and items that can be picked up(backpack, sticks, small rocks, letters), navigation options describe the next tiles can move and is dangerous? ( the environment and not moveable items,). The description of scene and navigation options will stay up until move to the next tile. "

    w = "W print( item_describe_one , item_describe_two ) the play area will be ringed by dangerous tiles. total grid five by five but playable would be four by four."

    a = "A if go out of bounds the player dies. If player move will do this give a warning and a chance to back out. To move, up minus four, right plus one, down plus four, left minus one to your index."

    s = "S print( item_describe_one , item_describe_two ) the play area will be ringed by dangerous tiles. total grid five by five but playable would be four by four."

    d = "D if go out of bounds the player dies. If player move will do this give a warning and a chance to back out. To move, up minus four, right plus one, down plus four, left minus one to your index."

    examine = ""
#   ctrl+l clears screen
    #print ("*"* 120)

    # if w scene and d return all blank spaces print d
    
    def cutup_string(self, block:int, string_to_cut:str, padding:int, beginning_index:int=0):
        """ Cuts up strings into chunks:
            need the length to chunk
            need the delimiter """
        
        index_cut = beginning_index + block
        if string_to_cut[-1] != " ":
            string_to_cut = string_to_cut + " "
        if index_cut > len(string_to_cut):
            index_cut = len(string_to_cut) -1
        if string_to_cut[index_cut] != " ":
            index_cut += 1
            if string_to_cut[index_cut] != " ":
                index_cut += 1
        while string_to_cut[index_cut] != " ":
            index_cut -= 1

        if string_to_cut[index_cut] == " ":
            cut_string = string_to_cut[beginning_index:index_cut].strip()

            padding = padding - len(cut_string)
            left_padding = padding /2
            right_padding = padding - int(left_padding)
            cut_string = int(left_padding) * " " + cut_string + right_padding * " "
            return cut_string ,index_cut

    def user_interface_one(self, north_south_examine):
        """ Used to rendering the top and bottom of the screen """     
        print()
        all_parts, one_index = self.cutup_string(50, north_south_examine, 100)
        all_parts
        print(all_parts)
        while not all_parts.isspace():
            print()
            all_parts, one_index = self.cutup_string(
                50, 
                north_south_examine, 
                100, 
                one_index)
            all_parts
            print(all_parts)
        print()

    def user_interface_three(self, west, scene, east):
        """ Will render three, the middle of the screen """
        print()
        p1, one_index = self.cutup_string(15, west, 20)
        p2, two_index = self.cutup_string(55, scene, 60)
        p3, three_index = self.cutup_string(15, east, 20)
        all_parts = p1+p2+p3
        print(all_parts)
        while not all_parts.isspace():
            p1, one_index = self.cutup_string(15, west, 20, one_index)
            p2, two_index = self.cutup_string(55, scene, 60, two_index)
            p3, three_index = self.cutup_string(15, east, 20, three_index)
            all_parts = p1+p2+p3
            print(all_parts)
        print()

if __name__ == "__main__":
    e = UserInterface()
    e.user_interface_three()