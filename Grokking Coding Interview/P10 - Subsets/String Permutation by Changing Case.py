def find_letter_case_string_permutations(str):
  permutations = []
  combinations = [[]]
  fit = len(str)

  for char in str:

      n = len(combinations)


      for _ in range(n):
          popped = combinations.pop(0)
          toAdd = list(popped)



          if char.isalpha():
              capitalize = list(toAdd)
              lower = list(toAdd)

              capitalize.append(char.capitalize())
              lower.append(char.lower())

              capitalize = "".join(capitalize)
              lower = "".join(lower)


              if len(capitalize) == fit:
                  permutations.append(capitalize)
                  permutations.append(lower)

              else:

                  combinations.append(capitalize)
                  combinations.append(lower)


          else:
              toAdd.append(char)
              toAdd = "".join(toAdd)
              if len(toAdd) == fit:
                  permutations.append(toAdd)

              else:
                  combinations.append(toAdd)


  return permutations


def main():
  print("String permutations are: " +
        str(find_letter_case_string_permutations("ad52")))
  print("String permutations are: " +
        str(find_letter_case_string_permutations("ab7c")))


main()
