document.addEventListener("DOMContentLoaded", function () {
	const form = document.getElementById("convert-form")

	form.addEventListener("submit", async function (event) {
		event.preventDefault()

		const fromCurrency = document.getElementById("from-currency").value
		const toCurrency = document.getElementById("to-currency").value
		const amount = parseFloat(document.getElementById("amount").value)

		try {
			const response = await fetch(
				`http://127.0.0.1:8000/convert?from_currency=${fromCurrency}&to_currency=${toCurrency}&amount-to-convert=${amount}`
			)

			if (!response.ok) {
				throw new Error("Error converting currency")
			}

			const result = await response.json()
			if (result && result.converted_amount !== undefined) {
				displayConvertedAmount(result)
			} else {
				throw new Error("Invalid conversion data")
			}
		} catch (error) {
			console.error("Failed to convert currency:", error)
			document.getElementById("conversion-result").textContent =
				"Failed to convert currency. Please try again later."
		}
	})

	function displayConvertedAmount(result) {
		const resultContainer = document.getElementById("conversion-result")
		const dateContainer = document.getElementById("conversion-date")

		resultContainer.innerHTML = `
            <p><strong>${result.amount} ${
			result.from_currency
		}</strong> equals <strong>${result.converted_amount.toFixed(2)} ${
			result.to_currency
		}</strong></p>
        `

		dateContainer.innerHTML = `
            <p><em>Conversion Date: ${result.convert_date}</em></p>
        `
	}
})
