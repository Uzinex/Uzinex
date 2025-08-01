import { useState, useEffect } from 'react';
import Loader from './Loader';

const PageWrapper = ({ children }) => {
  const [loading, setLoading] = useState(process.env.NODE_ENV !== 'test');

  useEffect(() => {
    if (process.env.NODE_ENV === 'test') return;
    const timer = setTimeout(() => setLoading(false), 400);
    return () => clearTimeout(timer);
  }, []);

  return loading ? <Loader /> : <div className="page-wrapper">{children}</div>;
};

export default PageWrapper;
