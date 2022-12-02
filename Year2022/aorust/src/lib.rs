use std::fs;

pub fn input_as_str(filepath : String) -> String{
    fs::read_to_string(filepath)
        .expect("Unable to open the file.")
}
