import '../styles/Footer.css';
import { useTranslation } from 'react-i18next';

const Footer = () => {
  const { t } = useTranslation();

  return (
    <footer className="footer">
      <p>{t('footer.rights')}</p>
      <div className="footer-links">
        <a href="https://t.me/uzinex" target="_blank" rel="noopener noreferrer">
          {t('contact.telegram')}
        </a>
        <a
          href="https://threads.net/@uzinex_official"
          target="_blank"
          rel="noopener noreferrer"
        >
          {t('contact.threads')}
        </a>
      </div>
    </footer>
  );
};

export default Footer;
