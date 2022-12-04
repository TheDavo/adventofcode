use std::collections::HashSet;
use itertools::Itertools;

pub fn solve_part_1() -> usize {
    let input = aorust::input_as_str(String::from("src/inputs/input3.txt"));

    input.lines().map(|rucksack| {
        let (left, right) = rucksack.split_at(rucksack.len() / 2);
        let hleft: HashSet<char> = HashSet::from_iter(left.chars());
        let hright: HashSet<char> = HashSet::from_iter(right.chars());
        let misplaced_item: Option<&char> = hleft.intersection(&hright).nth(0); // Option
        if let Some(item) = misplaced_item {
            get_item_priority(*item) 
        } else {
            0
        }
    }).sum()
}

pub fn solve_part_2() -> usize {
    let input = aorust::input_as_str(String::from("src/inputs/input3.txt"));    

    input.lines().tuples::<(_,_,_)>().map(|(first, second, third)| -> usize {
        let hfirst: HashSet<char> = HashSet::from_iter(first.chars());
        let hsecond: HashSet<char> = HashSet::from_iter(second.chars());

        let possible_badges = hfirst.intersection(&hsecond);
        possible_badges.map(|poss_badge| -> usize {
            match third.contains(*poss_badge) {
                true => get_item_priority(*poss_badge),
                false => 0,
            }
        }).sum::<usize>()
    }).sum::<usize>()
}

fn get_item_priority(item: char) -> usize {
    match item.is_uppercase() {
        true => item as usize - 'A' as usize + 27,
        false => item as usize - 'a' as usize + 1
    }
}
