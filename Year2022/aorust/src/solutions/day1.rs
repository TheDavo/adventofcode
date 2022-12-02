use std::fs;

pub fn solve_part_1() -> usize {
    let elf_foods = get_input();
    elf_foods
        .split("\n\n")
        .map(|elf| {
            elf.lines()
            .map(|cal_str| cal_str.parse::<usize>().unwrap())
            .sum::<usize>()
        })
        .max()
        .unwrap()
}

pub fn solve_part_2() -> usize {
    let elf_foods = get_input();
    let mut calc_cals : Vec<usize> = 
        elf_foods.split("\n\n")
        .map(|elf| {
            elf.lines()
            .map(|cal_str| cal_str.parse::<usize>().unwrap())
            .sum::<usize>()
        }).collect();
    calc_cals.sort();
    calc_cals.iter().rev().take(3).sum()
}

fn get_input() -> String {
    let file_path = "src/inputs/input1.txt";

    fs::read_to_string(file_path)
        .expect("Unable to open the file.")
}
