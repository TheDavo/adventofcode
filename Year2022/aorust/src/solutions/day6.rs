use itertools::Itertools;

fn find_unique_marker(input: &str, marker_size: usize) -> usize {
    let binding = input.chars().collect::<Vec<char>>();
    let tupled = binding.windows(marker_size);

    for (i, markers) in tupled.enumerate() {
        if markers.iter().all_unique() {
            return i + marker_size 
        }
    }
    0
}

pub fn solve_part_1() -> usize {
    let input = aorust::input_as_str(String::from("src/inputs/input6.txt"));
    find_unique_marker(&input, 4)
}

pub fn solve_part_2() -> usize {
    let input = aorust::input_as_str(String::from("src/inputs/input6.txt"));
    find_unique_marker(&input, 14)
}
