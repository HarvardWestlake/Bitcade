import "./CreatorsPage.css";

const creators = [
  "Ahren",
  "Arden",
  "Asher",
  "Gabe",
  "Daniel",
  "Bari",
  "AidanM",
  "Elysia",
  "AidanR",
  "Ben",
  "Ronan",
  "Chris",
  "Andrew",
  "Sarah",
  "Ryan",
  "Luke",
  "Manny",
  "JingJing",
  "Markus",
  "Oren",
  "Chris",
  "Mark",
  "Jake",
  "Sam",
  "Kian",
  "Sammy",
  "Wyatt",
  "WilliamA",
  "David",
  "Micha",
  "Chase",
  "Wyatt",
  "Alex",
  "Victor",
  "Natalie",
  "Ari",
  "Grady",
  "Claire",
  "Sophia",
  "MrTheiss",
  "MrLopez",
  "HarvardWestlake"
];

const CreatorsPage = () => {
  return (
    <div className="creators-page">
      <h1>Creators</h1>
      <p>This page is dedicated to the developers who created this project:</p>
      <ul className="creators-list">
        {creators.map((creator, index) => (
          <li key={index} className="creator-item">{creator}</li>
        ))}
      </ul>
    </div>
  );
};

export default CreatorsPage;
