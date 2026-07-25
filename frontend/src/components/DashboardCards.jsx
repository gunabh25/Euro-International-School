import { Users, Trophy, TrendingUp, TrendingDown } from "lucide-react";

export default function DashboardCards({ students }) {
  if (!students?.length) return null;

  const averages = students.map((s) => Number(s.average));

  const total = students.length;
  const avg =
    averages.reduce((a, b) => a + b, 0) / averages.length;

  const highest = Math.max(...averages);
  const lowest = Math.min(...averages);

  const cards = [
    {
      title: "Students",
      value: total,
      icon: <Users size={28} />,
      color: "bg-blue-500",
    },
    {
      title: "Average",
      value: avg.toFixed(1),
      icon: <TrendingUp size={28} />,
      color: "bg-green-500",
    },
    {
      title: "Highest",
      value: highest,
      icon: <Trophy size={28} />,
      color: "bg-yellow-500",
    },
    {
      title: "Lowest",
      value: lowest,
      icon: <TrendingDown size={28} />,
      color: "bg-red-500",
    },
  ];

  return (
    <div className="grid grid-cols-2 md:grid-cols-4 gap-5 mb-8">
      {cards.map((card) => (
        <div
          key={card.title}
          className="bg-white rounded-xl shadow-lg p-5 hover:shadow-xl transition"
        >
          <div className="flex justify-between items-center">
            <div>
              <p className="text-gray-500">{card.title}</p>
              <h2 className="text-3xl font-bold">{card.value}</h2>
            </div>

            <div
              className={`${card.color} text-white rounded-full p-3`}
            >
              {card.icon}
            </div>
          </div>
        </div>
      ))}
    </div>
  );
}