import { render, screen } from "@testing-library/react";
import App from "./App";

test("renders movie picture pipeline heading", () => {
  render(<App />);
  const heading = screen.getByText(/Movie Picture Pipeline/i);
  expect(heading).toBeInTheDocument();
});
