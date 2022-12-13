pub fn solve_part_1() -> usize {
    let elf_foods = aorust::input_as_str(String::from("src/inputs/input1.txt"));
    elf_foods
        .split("\r\n\r\n")
        .map(|elf| {
            elf.lines()
            .map(|cal_str| -> usize {cal_str.parse::<usize>().unwrap()})
            .sum::<usize>()
        })
        .max()
        .unwrap()
}

pub fn solve_part_2() -> usize {
    let elf_foods = aorust::input_as_str(String::from("src/inputs/input1.txt"));
    let mut calc_cals : Vec<usize> = 
        elf_foods.split("\r\n\r\n")
        .map(|elf| {
            elf.lines()
            .map(|cal_str| cal_str.parse::<usize>().unwrap())
            .sum::<usize>()
        }).collect();
    calc_cals.sort();
    calc_cals.iter().rev().take(3).sum()
}