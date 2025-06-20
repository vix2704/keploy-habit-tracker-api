document.addEventListener("DOMContentLoaded", () => {
  const habitList = document.getElementById("habit-list");
  const newHabitBtn = document.querySelector(".btn:nth-child(1)");
  const seeListBtn = document.querySelector(".btn:nth-child(2)");
  const deleteHabitBtn = document.querySelector(".btn:nth-child(3)");

  const BASE_URL = "https://keploy-habit-tracker-api.onrender.com";

  // Fetch and display habits
  async function fetchHabits() {
    try {
      const response = await fetch(`${BASE_URL}/habits/`);
      const habits = await response.json();

      habitList.innerHTML = ""; // Clear existing

      habits.forEach(habit => {
        const habitItem = document.createElement("div");
        habitItem.className = "habit";

        habitItem.innerHTML = `
          <span class="sparkle">✨</span>
          <div class="habit-name">${habit.name}</div>
          <div class="habit-desc">${habit.description}</div>
          <div class="checkboxes">
            ${[...Array(7)]
              .map((_, i) => `<input type="checkbox" class="day-check" title="Day ${i + 1}">`)
              .join("")}
          </div>
        `;

        habitList.appendChild(habitItem);
      });
    } catch (err) {
      console.error("Error fetching habits:", err);
    }
  }

  // Add new habit
  newHabitBtn.addEventListener("click", async () => {
    const name = prompt("Enter habit name:");
    const description = prompt("Enter habit description:");

    if (!name || !description) {
      alert("Both fields are required.");
      return;
    }

    try {
      const res = await fetch(`${BASE_URL}/habits/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          id: "string", // Placeholder
          name,
          description,
          is_complete: false
        })
      });

      if (res.ok) {
        alert("Habit added successfully!");
        fetchHabits();
      } else {
        alert("Failed to add habit.");
      }
    } catch (err) {
      console.error("Error adding habit:", err);
    }
  });

  // Delete habit
  deleteHabitBtn.addEventListener("click", async () => {
    const nameToDelete = prompt("Enter the exact name of the habit to delete:");

    if (!nameToDelete) return;

    try {
      const habits = await fetch(`${BASE_URL}/habits/`).then(res => res.json());
      const habit = habits.find(h => h.name === nameToDelete);

      if (!habit) {
        alert("Habit not found.");
        return;
      }

      const res = await fetch(`${BASE_URL}/habits/${habit._id}`, {
        method: "DELETE"
      });

      if (res.ok) {
        alert("Habit deleted.");
        fetchHabits();
      } else {
        alert("Failed to delete habit.");
      }
    } catch (err) {
      console.error("Error deleting habit:", err);
    }
  });

  // See List = re-fetch habits
  seeListBtn.addEventListener("click", fetchHabits);

  fetchHabits();
});
