import CSP_6_03_Writing_to_files as HW
def test_write_file():
    HW.writeFile(["These", "should", "different"], "inputwords.txt")
    assert open("inputwords.txt", "r").read() == "These\nshould\ndifferent"


def test_sort_names():
    HW.sortNames("Randomlist.txt", "Sortedlist.txt")  # must run before reading the file
    with open("Sortedlist.txt", "r") as f:
        sorted_names = [line.strip() for line in f if line.strip()]
    assert sorted_names == ["1", "2", "3", "4", "5","7"], f"sortNames failed: {sorted_names}"


def test_high_score():
    avg = HW.highScore(100)
    assert avg > 0, "highScore should return a positive average"
