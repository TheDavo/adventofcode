

#[derive(Debug)]
struct Instruction {
    amount: usize,
    from: usize,
    to: usize,
}
type Crates = Vec<char>;

fn get_crates(crates: &str) -> Vec<Crates> {
    let mut raw: Vec<_> = crates.lines().collect();
    let num_stacks = raw.pop().unwrap().split_ascii_whitespace().count();

    let mut crates: Vec<Crates> = vec![Vec::new(); num_stacks];
    raw 
        .iter()
        .rev()
        .flat_map(|row| {
            row.chars()
                .skip(1)
                .step_by(4)
                .enumerate()
                .filter(|(_, c)| !c.is_ascii_whitespace())
        })
        .for_each(|(i, c)| crates[i].push(c));

    crates
}

impl From<&str> for Instruction {
    fn from(s: &str) -> Self {
        let mut s = s.split_ascii_whitespace().skip(1).step_by(2);
        Instruction {
            amount: s.next().unwrap().parse::<usize>().unwrap(),
            from: s.next().unwrap().parse::<usize>().unwrap() - 1,
            to: s.next().unwrap().parse::<usize>().unwrap() - 1,
        }
    }
}

fn main () {
    println!("Day 5 Pt 1: {}", solve_part_1());
    println!("Day 5 Pt 2: {}", solve_part_2());
}

pub fn solve_part_1() -> String {
    let filepath = "src/inputs/input5.txt";
    let input = aorust::input_as_str(String::from(filepath));

    let (crates_str, procedure_str) = input.split_once("\r\n\r\n").unwrap();
    let mut crates: Vec<Crates> = get_crates(crates_str); 
    let procedure = procedure_str.lines().map(Instruction::from);

    procedure.for_each(|i: Instruction| {
        let remaining = crates[i.from].len() - i.amount;
        let mut popped = crates[i.from].split_off(remaining);
        popped.reverse();
        crates[i.to].append(&mut popped);
    });

    crates.iter().filter_map(|s| s.last()).collect()
}

pub fn solve_part_2() -> String {
    let filepath = "src/inputs/input5.txt";
    let input = aorust::input_as_str(String::from(filepath));

    let (crates_str, procedure_str) = input.split_once("\r\n\r\n").unwrap();
    let mut crates: Vec<Crates> = get_crates(crates_str); 
    let procedure = procedure_str.lines().map(Instruction::from);

    procedure.for_each(|i: Instruction| {
        let remaining = crates[i.from].len() - i.amount;
        let mut popped = crates[i.from].split_off(remaining);

        crates[i.to].append(&mut popped);
    });

    crates.iter().filter_map(|s| s.last()).collect()
}



