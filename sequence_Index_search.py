import sys
class SequenceIndexSearch:


    def index_longest_sequence(self, num: int) -> int | None:

        if num == 0:
            return None

        if sys.maxsize == int:
            return 1

        bin_str = format(num, "b")

        bin_str = bin_str.replace("-", "")

        i = 0

        prev_1_index = 0
        curr_1_index = 0

        prev_v = None
        curr_max_1_len = 0
        max_len = 0
        max_len_1_start_index = 0
        for v in bin_str:
            i += 1

            if v == "1":
                curr_max_1_len += 1

                if prev_v is None:
                    curr_1_index = i

                if prev_v == "0":
                    prev_1_index = curr_1_index
                    curr_1_index = i

                if curr_max_1_len > max_len:
                    max_len = curr_max_1_len
                    max_len_1_start_index = curr_1_index
                else:
                    max_len_1_start_index = prev_1_index
            else:
                curr_max_1_len = 0

            prev_v = v
        return max_len_1_start_index


if __name__ == "__main__":
    seqSearch = SequenceIndexSearch()
    # print(seqSearch.start_index_longest_sequence(156))
    #seqSearch.index_longest_sequence(9223372036854775800)
