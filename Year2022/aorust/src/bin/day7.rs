enum SystemNode {
    File,
    Directory,
}
struct File {
    size: i32,
    filename: String,
}

struct Directory {
    dirname: String,
    nodes: Vec<SystemNode>,
    parent: Option<String>,
}

struct Node {
    node_type: SystemNode,
    size: i32,
    name: String,
    parent: String,
}

fn main() {
    solve_part_1();
    //println!("Day 7 Pt 1: {}", solve_part_1());
    println!("Day 7 Pt 2: {}", solve_part_2());
}

pub fn solve_part_1() {
    let input = aorust::input_as_str(String::from("src/test_inputs/test_input7.txt"));
    let mut curdir = Directory {
        dirname: "/".to_string(),
        nodes: vec![],
        parent: None,
    };

    input.lines().skip(1).for_each(|line| {
        match line.split_ascii_whitespace().collect::<Vec<&str>>()[..] {
            ["$", "cd", ".."] => println!("changing dir .."),
            ["$", "cd", dir] => println!("{}", dir),
            ["$", "ls"] => println!("listing"),
            ["dir", dir] => println!("adding {} to current node", dir),
            [size, file] => {
                println!("adding file {} of size {} to current directory", file, size)
            }
            _ => panic!("unmatched pattern!"),
        }
    })
}

pub fn solve_part_2() -> usize {
    let input = aorust::input_as_str(String::from("src/inputs/input7.txt"));
    0
}
