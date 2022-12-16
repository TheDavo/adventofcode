#![allow(unused)]

use clap::Parser;
use std::process::Command;

#[derive(Parser)]
struct Cli {
    /// Day of Advent of Code to run
    day: usize,
}

fn main() {
    let args = Cli::parse();

    let mut day_str = format!("day{}", args.day);
    println!("{}", day_str);
    let mut output = Command::new("cargo");
    output
        .arg("run")
        .arg("--bin")
        .arg(day_str)
        .spawn()
        .expect("failed to execute process");
}
