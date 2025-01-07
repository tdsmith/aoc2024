use std::collections;
use std::env;
use std::fs;

fn part1(col1: &Vec<i32>, col2: &Vec<i32>) -> i32 {
    let mut my_col1 = col1.clone();
    let mut my_col2 = col2.clone();
    my_col1.sort();
    my_col2.sort();
    let answer: i32 = my_col1
        .iter()
        .zip(my_col2.iter())
        .map(|(c1, c2)| (c1 - c2).abs())
        .sum();
    answer
}

fn part2(col1: &Vec<i32>, col2: &Vec<i32>) -> i32 {
    let mut map = collections::HashMap::new();
    for v in col2 {
        let count = map.entry(v).or_insert(0);
        *count += 1;
    }
    let mut result = 0;
    for v in col1 {
        let count = map.get(v).unwrap_or(&0);
        result += v * count;
    }
    result
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let contents = fs::read_to_string(&args[1]).unwrap();
    let lines = contents.lines();
    let mut col1: Vec<i32> = Vec::new();
    let mut col2: Vec<i32> = Vec::new();

    for line in lines {
        let [a, b] = line
            .split_whitespace()
            .map(|x| x.parse().unwrap())
            .collect::<Vec<i32>>()
            .try_into()
            .unwrap();
        col1.push(a);
        col2.push(b);
    }

    println!("{}", part1(&col1, &col2));
    println!("{}", part2(&col1, &col2));
}
