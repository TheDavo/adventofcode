fn main () {
    println!("Day 4 Pt 1: {}", solve_part_1());
    println!("Day 4 Pt 2: {}", solve_part_2());
}

pub fn solve_part_1() -> usize {
    let input: String = aorust::input_as_str(String::from("src/inputs/input4.txt"));
    // let input: String = aorust::input_as_str(String::from("src/test_inputs/test_input4.txt")); 
    input.lines()
    .map(|assignment| -> (&str, &str) {assignment.split_once(',').unwrap()})
    .map(|(rng1, rng2)| -> ((usize, usize), (usize,usize)) {
        build_range(rng1, rng2)
    })
    .map(|(rng1, rng2)| contains(rng1, rng2))
    .filter(|contained| *contained)
    .count()
}

pub fn solve_part_2() -> usize {
    let input: String = aorust::input_as_str(String::from("src/inputs/input4.txt"));
    // let input: String = aorust::input_as_str(String::from("src/test_inputs/test_input4.txt")); 
    input.lines()
    .map(|assignment| -> (&str, &str) {assignment.split_once(',').unwrap()})
    .map(|(rng1, rng2)| -> ((usize, usize), (usize,usize)) {
        build_range(rng1, rng2)
    })
    .map(|(rng1, rng2)| overlaps(rng1, rng2))
    .filter(|contained| *contained)
    .count()
}

fn build_range(rng1: &str, rng2: &str) -> ((usize, usize), (usize, usize)) {
    let rng1_split = rng1.split_once('-').unwrap();
    let rng2_split = rng2.split_once('-').unwrap();
    ((rng1_split.0.parse().unwrap(), rng1_split.1.parse().unwrap()),
        (rng2_split.0.parse().unwrap(), rng2_split.1.parse().unwrap()))
}

// Returns whether rng1 is completely in rng2 or vice-versa
fn contains(rng1: (usize,usize), rng2: (usize, usize)) -> bool {
    (rng2.0 >= rng1.0 && rng2.1 <= rng1.1) || // is rng2 completely in rng1?
        (rng1.0 >= rng2.0 && rng1.1 <= rng2.1) // is rng1 completely in rng2?
}

fn overlaps(rng1: (usize,usize), rng2: (usize,usize)) -> bool {
    (rng1.1 >= rng2.0 && rng1.1 <= rng2.1) || 
    (rng1.0 <= rng2.1 && rng1.0 >= rng2.1) ||
    (rng2.0 >= rng1.0 && rng2.0 <= rng1.1) ||
    (rng2.1 >= rng1.0 && rng2.1 <= rng1.1)
}
