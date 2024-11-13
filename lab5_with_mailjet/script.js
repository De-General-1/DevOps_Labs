function heavyComputation() {
    while (true) {
        // Example of CPU-intensive task (calculating factorial)
        let result = 1;
        for (let i = 1; i <= 1000; i++) {
            result *= i;
            console.log(result)
        }
    }
}

// Start the heavy computation
heavyComputation();
