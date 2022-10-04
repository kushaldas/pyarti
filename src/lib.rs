use arti;
use pyo3::prelude::*;

#[pyfunction]
fn start_proxy() -> PyResult<bool> {
    let args = vec!["pyarti", "proxy"];
    arti::main_main(args).unwrap();
    Ok(true)
}

#[pymodule]
fn pyarti(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(start_proxy, m)?)?;
    Ok(())
}
