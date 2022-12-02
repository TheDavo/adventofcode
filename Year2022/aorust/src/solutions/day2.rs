enum GameResult {
    Win,
    Loss,
    Draw,
}

impl GameResult {
    fn get_game_result(elf_hand: &Hand, my_hand: &Hand) -> GameResult {
        match elf_hand {
            Hand::Rock => {
                match my_hand {
                    Hand::Rock => GameResult::Draw,
                    Hand::Paper => GameResult::Win,
                    Hand::Scissors => GameResult::Loss,
                }
            },
            Hand::Paper => {
                match my_hand {
                    Hand::Rock => GameResult::Loss,
                    Hand::Paper => GameResult::Draw,
                    Hand::Scissors => GameResult::Win,
                }
            },
            Hand::Scissors => {
                match my_hand {
                    Hand::Rock => GameResult::Win,
                    Hand::Paper => GameResult::Loss,
                    Hand::Scissors => GameResult::Draw,
                }
            },
        }
    }

    fn get_game_value(&self) -> usize {
        match self {
            GameResult::Draw => 3,
            GameResult::Loss => 0,
            GameResult::Win => 6,
        }
    }

    fn get_game_by_code(code : &str) -> GameResult {
        match code {
            "X" => GameResult::Loss,
            "Y" => GameResult::Draw,
            "Z" => GameResult::Win,
            _ => panic!("Not a valid game type!"),
        }
    }
}

enum Hand {
    Rock,
    Paper,
    Scissors,
}

impl Hand {
    fn new(hand : &str ) -> Hand{
        match hand {
            "A" | "X" => Hand::Rock,
            "B" | "Y" => Hand::Paper,
            "C" | "Z" => Hand::Scissors,
            _ => panic!("Not an expected RPS hand"),

        }
    }

    fn get_hand_value(&self) -> usize {
        match self {
            Hand::Rock => 1, 
            Hand::Paper => 2,
            Hand::Scissors => 3,
        }
    }

    fn get_hand_for_game_result(elf: Hand, game_res: &GameResult) -> Hand {
        match elf {
            Hand::Rock => {
                match game_res {
                    GameResult::Loss => Hand::Scissors,
                    GameResult::Draw => Hand::Rock,
                    GameResult::Win => Hand::Paper,
                }
            }
            Hand::Paper => {
                match game_res {
                    GameResult::Loss => Hand::Rock,
                    GameResult::Draw => Hand::Paper,
                    GameResult::Win => Hand::Scissors,
                }
            }
            Hand::Scissors => {
                match game_res {
                    GameResult::Loss => Hand::Paper,
                    GameResult::Draw => Hand::Scissors,
                    GameResult::Win => Hand::Rock,
                }
            }
        }
    }
}

pub fn solve_part_1() -> usize {
    let input = aorust::input_as_str(String::from("src/inputs/input2.txt"));
    let mut total_score : usize = 0;

    input.lines().for_each(|line| {
        let (elf_code, my_code) = line.split_once(" ").unwrap();
        let elf_hand: Hand = Hand::new(elf_code);
        let my_hand: Hand = Hand::new(my_code);

        let game_result: GameResult = GameResult::get_game_result(&elf_hand, &my_hand); 
        total_score += my_hand.get_hand_value() + game_result.get_game_value();
    });
    
    total_score
}

pub fn solve_part_2() -> usize {
    let input = aorust::input_as_str(String::from("src/inputs/input2.txt"));
    let mut total_score : usize = 0;

    input.lines().for_each(|line| {
        let (elf_code, game_code) = line.split_once(" ").unwrap();
        let elf_hand: Hand = Hand::new(elf_code);
        let game: GameResult = GameResult::get_game_by_code(game_code);
        let my_hand: Hand = Hand::get_hand_for_game_result(elf_hand, &game);
        total_score += my_hand.get_hand_value() + game.get_game_value();
    });
    
    total_score
}
