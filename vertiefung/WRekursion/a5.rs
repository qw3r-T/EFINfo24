use std::io;

// i : anzahl klötze die bewegt werden
// a : der stab von dem verschoben werden soll
// b : der stab welcher als zwischen ziel dient
// c : der stab auf dem die scheiben verschoben werden sollen
fn mov(i: u32, a: &str, b: &str, c: &str) {
    if i>0 {
        mov(i-1, a, c, b);
        println!("{} -> {}",a,c);
        mov(i-1, b, a, c);
    }
}

fn main() {
    println!("Please enter a number:");
    
    let mut input =  String::new();
    io::stdin().read_line(&mut input).expect("Failed to read line");
    let input: u32 = input.trim().parse().expect("You didn't enter a number");
    
    mov(input,"Links","Mitte","Rechts");
}