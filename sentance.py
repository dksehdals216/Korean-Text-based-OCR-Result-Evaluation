
def morph(original):

    with open('data/' + original) as f:
        content = f.readlines()

        content = [x.strip() for x in content]

        with open('data/data_by_line/' + original + "_line", 'w') as _f:
            for line in content:
                if line:
                    _f.write(line)
                    _f.write("\n")

def main():
    morph('mine_orig')
    morph('mine_tess')
    morph('prof_orig')
    morph('prof_tess')
    morph('dudu1_orig')
    morph('dudu1_tess')
    morph('dudu2_orig')
    morph('dudu2_tess')


if __name__ == "__main__":
    main()
