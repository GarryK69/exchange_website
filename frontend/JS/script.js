document.addEventListener("DOMContentLoaded", function () {
	// Функция для загрузки курсов валют
	async function loadCurrencyRates() {
		try {
			const response = await fetch("http://127.0.0.1:8000/currency")
			if (!response.ok) {
				throw new Error("Error fetching exchange rates")
			}
			const exchangeRates = await response.json()
			displayCurrencyRate("UAH", exchangeRates) // Выводим только UAH
		} catch (error) {
			console.error("Failed to load currency rates:", error)
			document.getElementById("currency-r").innerHTML = `
							<p>Failed to load currency rates. Please try again later.</p>
					`
		}
	}

	// Функция для отображения курса валют
	function displayCurrencyRate(currencyCode, rates) {
		const currencyContainer = document.getElementById("currency-r")
		const rate = rates[currencyCode]
		const date = new Date().toLocaleDateString()

		if (rate !== undefined) {
			currencyContainer.innerHTML = `
							<p><strong>USD to ${currencyCode}:</strong> ${rate.toFixed(2)}</p>
							<p><em>Last updated: ${date}</em></p>
					`
		} else {
			currencyContainer.innerHTML = `
							<p>Rate for ${currencyCode} not available</p>
					`
		}
	}

	// Загрузить курсы валют при загрузке страницы
	loadCurrencyRates()
})
