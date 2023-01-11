extern crate scraper;
extern crate reqwest;
use std::{thread, time};
use std::fs::File;
use std::io::prelude::*;


fn main() {

    scrape_rate("https://lirarate.org/")

}

fn scrape_rate(url: &str) {

    loop {
        
        let req = reqwest::blocking::get(url).unwrap();
        let body = scraper::Html::parse_document(&req.text().unwrap());

        let qty = scraper::Selector::parse("p").unwrap();
        let mut count: i8 = 0;
        let mut file = File::create(r"C:\Users\johnc\Documents\CP2\scraper\scrape\src\rate.txt").expect("Failed.");

        for qty in body.select(&qty) {
            if count == 2 {
                break;
            }
            let qtys = qty.text().collect::<Vec<_>>();
            let num: Vec<&str> = qtys[1].split(" ").collect();
            let info = format!("{}: {}", qtys[0], num[4]);
            file.write_all(info.as_bytes()).expect("Failed.");
            file.write_all(b"\n").expect("Failed.");
            count += 1;
        }
        thread::sleep(time::Duration::from_secs(1800));
    }
}
