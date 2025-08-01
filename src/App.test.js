import { render, screen } from '@testing-library/react';
import App from './App.jsx';

jest.mock('react-router-dom', () => ({
  BrowserRouter: ({ children }) => <div>{children}</div>,
  Routes: ({ children }) => <div>{children}</div>,
  Route: ({ element }) => <>{element}</>,
}), { virtual: true });

test('renders main heading', () => {
  render(<App />);
  const heading = screen.getByRole('heading', { level: 1 });
  expect(heading).toBeInTheDocument();
});
